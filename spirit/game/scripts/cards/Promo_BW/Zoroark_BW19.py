from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import debuff_defender_attacks
from spirit.game.card_effects.attacks_common import bonus_if, active_is
from spirit.game.session.effects import is_stage2_pokemon


card = PokemonCardDef(
    guid="49d9108a-bb3a-5d8c-938a-e38cc80c30d4",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    display_name="Zoroark",
    searchable_by=["Zoroark", "Stage 1", "Zoroark"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Attack(
            title="Punishment",
            game_text="If the Defending Pok\u00e9mon is a Stage 2 Pok\u00e9mon, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(active_is(is_stage2_pokemon), 20),
        ),
        Attack(
            title="Snarl",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 20 (before applying Weakness and Resistance).",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=debuff_defender_attacks(20),
        ),
    ],
)