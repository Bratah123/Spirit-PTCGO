from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.session.passives import Passive, active_passives


class DarkAuraPassive(Passive):
    """All Energy attached to this Pokemon are Darkness Energy."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None:
            return options
        for passive, carrier in active_passives(board):
            if isinstance(passive, DarkAuraPassive) and carrier is holder:
                return [[PokemonTypes.DARKNESS.value]]
        return options


card = PokemonCardDef(
    guid="a6672b87-cd52-56f0-83de-30bb1084c53c",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon", "Stage 2", "Hydreigon"],
    subtypes=["Stage 2"],
    collector_number=103,
    set_code="BW4",
    rarity=Rarities.RareSecret,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=635,
    abilities=[
        Ability(
            title="Dark Aura",
            game_text="All Energy attached to this Pok\u00e9mon are Darkness Energy instead of their usual type.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=DarkAuraPassive(),
        ),
        Attack(
            title="Berserker Blade",
            game_text="Does 40 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 4},
            damage=60,
            effect=snipe_attack(40, pool='bench', count=2, also_base=True),
        ),
    ],
)