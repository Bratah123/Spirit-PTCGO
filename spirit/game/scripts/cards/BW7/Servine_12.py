from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="5583feb5-ea05-5de5-aeca-46977d809e9c",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    display_name="Servine",
    searchable_by=["Servine", "Stage 1", "Servine"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snivy.Name",
    family_id=495,
    abilities=[
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Double Slash",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            effect=flip_damage(2, per_heads=40),
        ),
    ],
)