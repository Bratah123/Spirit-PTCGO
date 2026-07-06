from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="685ebc6c-a630-52be-85f4-698bb2b2960b",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektross.Name",
    display_name="Eelektross",
    searchable_by=["Eelektross", "Stage 2", "Eelektross"],
    subtypes=["Stage 2"],
    collector_number=59,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    family_id=602,
    abilities=[
        Attack(
            title="Electrified Bite Mark",
            game_text="During your opponent's next turn, if they attach an Energy card from their hand to the Defending Pok\u00e9mon, put 6 damage counters on that Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Electro Sprinkler",
            game_text="This attack also does 30 damage to 1 of your Benched Pok\u00e9mon and 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)