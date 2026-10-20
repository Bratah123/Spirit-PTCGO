from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import heal_attack


async def _prehistoric_call(ctx):
    """Once during your turn, if this Pokemon is in your discard pile, you may
    put it on the bottom of your deck."""
    await ctx.put_on_bottom_of_deck(ctx.source)


card = PokemonCardDef(
    guid="d7557a9d-064d-57cf-a4cd-93b75593ff05",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    display_name="Lileep",
    searchable_by=["Lileep", "Restored", "Lileep"],
    subtypes=["Restored"],
    collector_number=3,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.RESTORED,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RootFossilLileep.Name",
    family_id=345,
    abilities=[
        Ability(
            title="Prehistoric Call",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your discard pile, you may put this Pok\u00e9mon on the bottom of your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            usable_from="discard",
            effect=_prehistoric_call,
        ),
        Attack(
            title="Spiral Drain",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=heal_attack(10),
        ),
    ],
)