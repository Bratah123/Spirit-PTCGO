from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon, effective_max_hp
from spirit.game.attributes import AttrID

class HealingBerryPassive(Passive):
    """At end of any turn, if holder has 20 HP or less, heal 30 and discard this."""
    pass

async def healing_berry_eot(ctx):
    tool = ctx.source
    pokemon = carrier_pokemon(tool)
    if pokemon is None:
        return
    hp = pokemon.get_attribute(AttrID.HP, 0)
    if hp > 20:
        return
    await ctx.heal(pokemon, 30)
    await ctx.discard_cards([tool])

card = PokemonToolCardDef(
    guid="ba5d9837-f689-5a9f-94aa-a7106fda5b18",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HealingBerry.Name",
    display_name="Healing Berry",
    searchable_by=["Healing Berry", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=125,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    passive=HealingBerryPassive(),
    abilities=[
        Ability(
            title="Healing Berry",
            game_text="At the end of any turn, if the Pokémon this card is attached to has 20 HP or less, remove 3 damage counters from that Pokémon and discard this card.",
            trigger=Triggers.END_OF_TURN,
            effect=healing_berry_eot,
        ),
    ],
)
