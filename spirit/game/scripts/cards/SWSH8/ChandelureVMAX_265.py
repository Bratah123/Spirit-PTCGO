from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, TrainerType
from spirit.game.session.effects import is_trainer_card
from spirit.game.session.passives import Passive
from spirit.game.card_effects.passives_common import is_in_active_spot


class CursedShimmerPassive(Passive):
    def blocks_trainer_play(self, card, player_id, carrier):
        if player_id == carrier.owning_player_id:
            return False
        if not is_in_active_spot(carrier):
            return False
        return card.get_attribute(AttrID.TRAINER_TYPE) in (
            TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value,
        )


async def max_poltergeist(ctx):
    """Opponent reveals hand; 70 damage for each Trainer card found there."""
    hand = await ctx.reveal_hand(ctx.opponent_id)
    count = sum(1 for c in hand if is_trainer_card(c))
    await ctx.deal_damage(70 * count)


card = PokemonCardDef(
    guid="205a08f9-5a0d-5790-9e0f-3e4a6400e7c6",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChandelureVMAX.Name",
    display_name="Chandelure VMAX",
    searchable_by=["Chandelure VMAX", "VMAX", "ChandelureVMAX"],
    subtypes=["VMAX"],
    collector_number=265,
    set_code="SWSH8",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ChandelureV.Name",
    family_id=609,
    abilities=[
        Ability(
            title="Cursed Shimmer",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent can't play any Pok\u00e9mon Tool cards from their hand.",
            passive=CursedShimmerPassive(),
        ),
        Attack(
            title="Max Poltergeist",
            game_text="Your opponent reveals their hand. This attack does 70 damage for each Trainer card you find there.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=max_poltergeist,
        ),
    ],
)