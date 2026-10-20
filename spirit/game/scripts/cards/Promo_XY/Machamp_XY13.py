from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.passives_common import team_damage_boost_passive, debuff_defender_attacks


def _is_fighting(card):
    return PokemonTypes.FIGHTING.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="41d95f3a-d491-5287-b9f7-e2464dcbc0eb",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Fighting Fury",
            game_text="Each of your Fighting Pok\u00e9mon's attacks do 20 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=team_damage_boost_passive(20, attacker_pred=_is_fighting),
        ),
        Attack(
            title="Machamp Crush",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 40 (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 3},
            damage=80,
            effect=debuff_defender_attacks(40),
        ),
    ],
)