from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class BossPocketsPassive(Passive):
    def tool_capacity(self, pokemon, carrier):
        return 4 if pokemon is carrier else 1


async def fearsome_shadow(ctx):
    """Your opponent reveals their hand."""
    await ctx.deal_damage()
    await ctx.reveal_hand(of_player=ctx.opponent_id)


card = PokemonCardDef(
    guid="f89cd2ae-9915-5fc8-a159-0d66cbe1c5bf",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HonchkrowV.Name",
    display_name="Honchkrow V",
    searchable_by=["Honchkrow V", "Basic", "V", "HonchkrowV"],
    subtypes=["Basic", "V"],
    collector_number=161,
    set_code="SWSH9",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=430,
    abilities=[
        Ability(
            title="Boss Pockets",
            game_text="This Pok\u00e9mon may have up to 4 Pok\u00e9mon Tools attached to it. If it loses this Ability, discard Pok\u00e9mon Tools from it until only 1 remains.",
            passive=BossPocketsPassive(),
        ),
        Attack(
            title="Fearsome Shadow",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=fearsome_shadow,
        ),
    ],
)