from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import mega_drain
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="380a017e-d722-58a6-b55a-7ba2ff77e230",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Butterfree.Name",
    display_name="Butterfree",
    searchable_by=["Butterfree", "Stage 2", "Butterfree"],
    subtypes=["Stage 2"],
    collector_number=21,
    set_code="BASE6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    family_id=10,
    abilities=[
        Attack(
            title="Whirlwind",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon, if any. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Mega Drain",
            game_text="Remove a number of damage counters from Butterfree equal of half the damage done to the Defending Pok\u00e9mon (after applying Weakness and Resistance) (rounded up to the nearest 10). If Butterfree has fewer damage counters that that, remove all of them.",
            cost={PokemonTypes.GRASS: 4},
            damage=40,
            effect=mega_drain,
        ),
    ],
)
