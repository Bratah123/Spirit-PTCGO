from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Triggers
from spirit.game.card_effects.attacks_common import recoil_attack

from spirit.game.data_utils import Triggers


async def fresh_egg(ctx):
    """On evolve: you may heal 80 damage from your Active Pokémon."""
    active = ctx.my_active()
    if active is None:
        return
    if await ctx.ask_yes_no("Heal 80 damage from your Active Pokémon?"):
        await ctx.heal(80, active)


card = PokemonCardDef(
    guid="6f97857b-63e5-5c68-b272-8b84b9539a6d",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name",
    display_name="Blissey",
    searchable_by=["Blissey", "Stage 1", "Blissey"],
    subtypes=["Stage 1"],
    collector_number=102,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=113,
    abilities=[
        Ability(
            title="Fresh Egg",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may heal 80 damage from your Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=fresh_egg,
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pok\u00e9mon does 80 damage to itself.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=160,
            effect=recoil_attack(80),
        ),
    ],
)