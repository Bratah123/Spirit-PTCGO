from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import TypedDamageBoostPassive


card = PokemonCardDef(
    guid="16fe273d-51d3-523c-a171-c577fc0d2584",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Keldeo.Name",
    display_name="Keldeo",
    searchable_by=["Keldeo", "Basic", "Keldeo"],
    subtypes=["Basic"],
    collector_number=191,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=647,
    abilities=[
        Ability(
            title="Justified",
            game_text="This Pok\u00e9mon's attacks do 50 more damage to your opponent's Darkness Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=TypedDamageBoostPassive(PokemonTypes.DARKNESS, 50, to_active_only=False),
        ),
        Attack(
            title="Sacred Sword",
            game_text="This Pok\u00e9mon can't use Sacred Sword during your next turn.",
            cost={PokemonTypes.WATER: 3},
            damage=100,
            effect=None,
            locks_next_turn=True,
        ),
    ],
)