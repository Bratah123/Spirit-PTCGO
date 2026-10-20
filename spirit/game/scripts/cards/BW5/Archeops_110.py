from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="0fe71072-318d-503b-8700-d39a84909b92",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archeops.Name",
    display_name="Archeops",
    searchable_by=["Archeops", "Stage 1", "Archeops"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="BW5",
    rarity=Rarities.RareSecret,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Archen.Name",
    family_id=567,
    abilities=[
        Ability(
            title="Ancient Power",
            game_text="Each play can't play any Pok\u00e9mon from his or her hand to evolve his or her Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Rock Slide",
            game_text="Does 10 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)