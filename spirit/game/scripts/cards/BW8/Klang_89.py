from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="46fde3ad-cb9b-590a-842f-d748068b3a14",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    display_name="Klang",
    searchable_by=["Klang", "Stage 1", "Klang"],
    subtypes=["Stage 1"],
    collector_number=89,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klink.Name",
    family_id=599,
    abilities=[
        Attack(
            title="Vice Grip",
            cost={PokemonTypes.METAL: 1},
            damage=20,
        ),
        Attack(
            title="Gear Smash",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=20),
        ),
    ],
)