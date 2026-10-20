from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="c4a5e019-376e-56a9-b4d5-8610a4d8cf78",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skorupi.Name",
    display_name="Skorupi",
    searchable_by=["Skorupi", "Basic", "Skorupi"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="XY9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=451,
    abilities=[
        Attack(
            title="Pin Missile",
            game_text="Flip 4 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(4, per_heads=10),
        ),
    ],
)