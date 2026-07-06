from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b528a4e5-1d04-5dc6-a5fc-877f8d62872c",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SkuntankV.Name",
    display_name="Skuntank V",
    searchable_by=["Skuntank V", "Basic", "V", "SkuntankV"],
    subtypes=["Basic", "V"],
    collector_number=181,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=435,
    abilities=[
        Attack(
            title="Pursuit Blast",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. If that Pok\u00e9mon retreated from the Active Spot during your opponent's last turn, this attack does 120 damage instead. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Shrieking Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=unimplemented,
        ),
    ],
)