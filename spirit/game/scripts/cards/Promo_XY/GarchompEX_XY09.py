from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, self_energy_discard_attack


card = PokemonCardDef(
    guid="849da797-6d6b-5fad-bdf7-b406a6701921",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompEX.Name",
    display_name="Garchomp-EX",
    searchable_by=["Garchomp-EX", "Basic", "EX", "GarchompEX"],
    subtypes=["Basic", "EX"],
    collector_number=9,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=445,
    abilities=[
        Attack(
            title="Dual Chop",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
        Attack(
            title="Power Blast",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)