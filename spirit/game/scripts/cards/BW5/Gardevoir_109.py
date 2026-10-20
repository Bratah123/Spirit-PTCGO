from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.passives import Passive, active_passives, effective_pokemon_types


class PsychicMiragePassive(Passive):
    """Each basic Psychic Energy attached to your Psychic Pokémon provides
    Psychic Psychic; multiple copies don't stack."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or energy.get_attribute(AttrID.IS_SPECIAL_ENERGY):
            return options
        if not energy_provides_type(energy, PokemonTypes.PSYCHIC.value):
            return options
        if any(len(option) >= 2 for option in options):
            return options
        if PokemonTypes.PSYCHIC.value not in effective_pokemon_types(board, holder):
            return options
        # Only the first Psychic Mirage in the passive list applies.
        for passive, carrier in active_passives(board):
            if isinstance(passive, PsychicMiragePassive) and \
                    carrier.owning_player_id == holder.owning_player_id:
                if passive is not self:
                    return options
                return [list(option) * 2 for option in options]
        return options


async def mind_shock(ctx):
    """Printed damage, not affected by Weakness or Resistance."""
    await ctx.deal_damage(apply_modifiers=False)


card = PokemonCardDef(
    guid="bbb64b16-321e-5d5a-9469-0eebfe5900cb",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir",
    searchable_by=["Gardevoir", "Stage 2", "Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=109,
    set_code="BW5",
    rarity=Rarities.RareSecret,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=282,
    abilities=[
        Ability(
            title="Psychic Mirage",
            game_text="Each basic Psychic Energy attached to your Psychic Pok\u00e9mon provides PsychicPsychic Energy. You can't apply more than 1 Psychic Mirage Ability at a time.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=PsychicMiragePassive(),
        ),
        Attack(
            title="Mind Shock",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=mind_shock,
        ),
    ],
)