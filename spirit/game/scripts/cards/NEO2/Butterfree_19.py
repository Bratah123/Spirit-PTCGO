from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import hyper_reverse, magic_pollen


card = PokemonCardDef(
    guid="a90c69a6-4aa7-5360-a3c7-09d9541e585b",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Butterfree.Name",
    display_name="Butterfree",
    searchable_by=["Butterfree", "Stage 2", "Butterfree"],
    subtypes=["Stage 2"],
    collector_number=19,
    set_code="NEO2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    family_id=10,
    abilities=[
        Attack(
            title="Magic Dust",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now either Asleep, Confused, Paralyzed, or Poisoned (your choice).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=magic_pollen,
        ),
        Attack(
            title="Hyper Reverse",
            game_text="Does 10 damage times the number of Energy attached to the Defending Pok\u00e9mon. After doing damage, remove a number of damage counters from Butterfree equal to the amount of damage done to the Defending Pok\u00e9mon (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            effect=hyper_reverse,
        ),
    ],
)
