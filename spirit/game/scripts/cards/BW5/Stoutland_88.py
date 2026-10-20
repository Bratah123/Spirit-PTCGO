from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="10a584df-641e-591e-a16f-5fbe4e7df577",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name",
    display_name="Stoutland",
    searchable_by=["Stoutland", "Stage 2", "Stoutland"],
    subtypes=["Stage 2"],
    collector_number=88,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    family_id=506,
    abilities=[
        Attack(
            title="Special Fang",
            game_text="If this Pok\u00e9mon has a Special Energy attached to it, this attack does 40 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Ferocious Bellow",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 30 (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            effect=unimplemented,
        ),
    ],
)