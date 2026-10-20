from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2bd7187d-e1f2-5d62-8dd0-145b394023a9",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name",
    display_name="Garbodor",
    searchable_by=["Garbodor", "Stage 1", "Team Plasma", "Garbodor"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=67,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    family_id=568,
    abilities=[
        Attack(
            title="Ensnarl",
            game_text="Does 20 damage times the number of Colorless in the Defending Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Double Ducts",
            game_text="Flip 2 coins. This attack does 80 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)