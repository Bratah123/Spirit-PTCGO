from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm12 import disk_reload, disk_reload_condition
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.sm8 import sublimation_gx


def _supporter_played_this_turn(ctx):
    return ctx.supporters_played_this_turn() > 0


card = PokemonCardDef(
    guid="9f5ae7c2-cc6c-564d-92bd-3c266f8fb9a8",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SilvallyGX.Name",
    display_name="Silvally-GX",
    searchable_by=["Silvally-GX", "Stage 1", "GX", "SilvallyGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=262,
    set_code="SM12",
    rarity=Rarities.RareRainbow,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name",
    family_id=772,
    abilities=[
        Ability(
            title="Disk Reload",
            game_text="Once during your turn (before your attack), you may draw cards until you have 5 cards in your hand.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=disk_reload_condition,
            effect=disk_reload,
        ),
        Attack(
            title="Brave Buddies",
            game_text="If you played a Supporter card from your hand during this turn, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(_supporter_played_this_turn, 70),
        ),
        Attack(
            title="Silver Knight-GX",
            game_text="If your opponent's Active Pok\u00e9mon is an Ultra Beast, it is Knocked Out. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=sublimation_gx,
        ),
    ],
)