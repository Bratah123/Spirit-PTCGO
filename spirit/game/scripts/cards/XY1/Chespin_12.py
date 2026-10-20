from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="515ee303-bb06-5674-a48a-3a729c4b5b9c",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chespin.Name",
    display_name="Chespin",
    searchable_by=["Chespin", "Basic", "Chespin"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=650,
    abilities=[
        Attack(
            title="Pin Missile",
            game_text="Flip 4 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(4, per_heads=10),
        ),
    ],
)