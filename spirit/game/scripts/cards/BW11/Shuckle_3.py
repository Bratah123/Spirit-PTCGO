from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.support_common import heal_targets


card = PokemonCardDef(
    guid="6ec4b7a5-01ba-5008-ba5d-bea36532d08e",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name",
    display_name="Shuckle",
    searchable_by=["Shuckle", "Basic", "Shuckle"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=213,
    abilities=[
        Attack(
            title="Share",
            game_text="Heal 40 damage from 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=heal_targets(40, "bench_choice"),
        ),
        Attack(
            title="Double Stab",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=flip_damage(2, per_heads=40),
        ),
    ],
)