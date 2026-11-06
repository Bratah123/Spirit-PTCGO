from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import boost_own_next_turn


card = PokemonCardDef(
    guid="67aa242b-6556-5b28-86c4-4841cbd6536c",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Keldeo.Name",
    display_name="Keldeo",
    searchable_by=["Keldeo", "Basic", "Keldeo"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=647,
    abilities=[
        Attack(
            title="Swords Dance",
            game_text="During your next turn, this Pok\u00e9mon's Aqua Blade attack's base damage is 120.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=boost_own_next_turn(60, attack_title='Aqua Blade'),
        ),
        Attack(
            title="Aqua Blade",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)