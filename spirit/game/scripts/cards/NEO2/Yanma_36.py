from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import shockwave, swift


card = PokemonCardDef(
    guid="5ecda8c7-883d-570b-bca8-6f5517effd2b",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    display_name="Yanma",
    searchable_by=["Yanma", "Basic", "Yanma"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="NEO2",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=193,
    abilities=[
        Attack(
            title="Shockwave",
            game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Pok\u00e9mon. Don't apply Weakness and Resistance. Then, if your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and switches it with the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=shockwave,
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9mon Powers, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            effect=swift,
        ),
    ],
)
