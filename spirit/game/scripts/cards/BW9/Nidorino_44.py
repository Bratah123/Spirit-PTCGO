from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="45327383-a186-53d7-8df5-24c56d06faa1",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    display_name="Nidorino",
    searchable_by=["Nidorino", "Stage 1", "Nidorino"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name",
    family_id=32,
    abilities=[
        Attack(
            title="Double Kick",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
        Attack(
            title="Horn Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)