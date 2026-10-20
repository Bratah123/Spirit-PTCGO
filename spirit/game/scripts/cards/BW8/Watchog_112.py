from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ab7e4d53-e91d-5466-bb31-d76936b65429",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Watchog.Name",
    display_name="Watchog",
    searchable_by=["Watchog", "Stage 1", "Team Plasma", "Watchog"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=112,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    family_id=504,
    abilities=[
        Attack(
            title="Fast Swipe",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Biting Fang",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)