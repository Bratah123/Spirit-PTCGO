from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import triple_spin


card = PokemonCardDef(
    guid="c98afd75-c758-598d-aea0-50634603a041",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmontop.Name",
    display_name="Hitmontop",
    searchable_by=["Hitmontop", "Basic", "Hitmontop"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=237,
    abilities=[
        Attack(
            title="Double Kick",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=20),
        ),
        Attack(
            title="Triple Spin",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads. If you get 2 or more heads, switch Hitmontop with 1 of your Benched Pok\u00e9mon, if any.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=triple_spin,
        ),
    ],
)
