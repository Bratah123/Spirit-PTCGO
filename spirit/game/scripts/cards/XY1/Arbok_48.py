from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive


class _NoAbilities(Passive):
    """The carrier (the Defending Pokemon) has no Abilities."""
    def blocks_abilities(self, pokemon, carrier):
        return pokemon is carrier


async def _gastro_acid(ctx):
    """20; the Defending Pokemon has no Abilities until the end of your next turn."""
    await ctx.deal_damage()
    target = ctx.defender
    if target is not None and not ctx.effects_blocked(target):
        ctx.add_passive_through_own_next_turn(target, _NoAbilities())


card = PokemonCardDef(
    guid="239d53c9-a709-5809-9a73-475bffb5a909",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arbok.Name",
    display_name="Arbok",
    searchable_by=["Arbok", "Stage 1", "Arbok"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    family_id=23,
    abilities=[
        Attack(
            title="Gastro Acid",
            game_text="The Defending Pok\u00e9mon has no Abilities until the end of your next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_gastro_acid,
        ),
        Attack(
            title="Poison Jab",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)