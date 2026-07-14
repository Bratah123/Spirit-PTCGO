from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.passives_common import takes_less_passive, is_in_active_spot


def _sparkle_veil_protects(target, carrier):
    return target.owning_player_id == carrier.owning_player_id and is_in_active_spot(carrier)


def _supporter_played_this_turn(ctx):
    return ctx.supporters_played_this_turn() > 0


card = PokemonCardDef(
    guid="a89e5e42-398b-5c49-ba16-a24d79af8079",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diancie.Name",
    display_name="Diancie",
    searchable_by=["Diancie", "Basic", "Diancie"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="SWSH4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=719,
    abilities=[
        Ability(
            title="Sparkle Veil",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, any damage done to your Pok\u00e9mon by an opponent's attack is reduced by 30 (after applying Weakness and Resistance).",
            passive=takes_less_passive(30, protects=_sparkle_veil_protects),
        ),
        Attack(
            title="Sensitive Ray",
            game_text="If you played a Supporter card from your hand during this turn, this attack does 70 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(_supporter_played_this_turn, 70),
        ),
    ],
)