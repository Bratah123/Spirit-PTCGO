from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import reduce_if_defending_attacks


card = PokemonCardDef(
    guid="17baa5e2-bba8-51ab-8529-d0315ec0d410",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name",
    display_name="Persian",
    searchable_by=["Persian", "Stage 1", "Persian"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    family_id=52,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Pounce",
            game_text="If the Defending Pok\u00e9mon attacks Persian during your next turn, any damage done by the attack is reduced by 10 (after applying Weakness and Resistance). (Benching either Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=reduce_if_defending_attacks(10),
        ),
    ],
)
