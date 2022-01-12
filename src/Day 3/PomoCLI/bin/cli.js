#! /usr/bin/env node

import inquirer from 'inquirer';
import chalk from 'chalk';
import shell from 'shelljs';
import cliProgress from 'cli-progress';
import notifier from 'node-notifier';
import { create } from 'timrjs'

const path = process.cwd()

import questions from './utils/questions.js';

inquirer.prompt(questions).then((answers) => {
    const timeWorkSeconds = answers.sessionWorkDuration * 60
    const timeBreakSeconds = answers.sessionBreakDuration * 60

    const workTimer = create(timeWorkSeconds)
    workTimer.start()

    const workBar = new cliProgress.Bar()
    workBar.start(timeWorkSeconds, 0);
    let workValue = 0;
    const timer = setInterval(function () {
        workValue++;
        workBar.update(workValue)
        if (workValue >= workBar.getTotal()) {
            clearInterval(timer);
            workBar.stop();
        }
    }, 1000);

    workTimer.finish(() => {
        notifier.notify({
            title: "PomoCLI 🍅",
            message: "The work session is been completed, get some break"
        })
        const breakTimer = create(timeBreakSeconds)
        breakTimer.start()
        const breakBar = new cliProgress.Bar()
        breakBar.start(timeBreakSeconds, 0)
        let breakValue = 0;
        const timer = setInterval(function () {
            breakValue++;
            breakBar.update(breakValue)
            if (breakValue >= breakBar.getTotal()) {
                clearInterval(timer);
                breakBar.stop();
            }
        }, 1000);
    })
})