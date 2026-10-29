from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="7c1a1d9c-6778-5317-ac73-8223bbd7101a",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name",
    display_name="Skiddo",
    searchable_by=["Skiddo", "Basic", "Skiddo"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=672,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(1),
        ),
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)