from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.trainers import is_basic_energy_card


class _EnergyKeeper(Passive):
    """Basic Energy on your Basic Pokemon can't be discarded by your opponent's effects
    (the engine hook covers opposing Item/Supporter moves)."""
    def blocks_energy_removal(self, energy, mover_player_id, carrier):
        me = carrier_pokemon(carrier)
        holder = getattr(energy, "parent", None)
        return (me is not None and holder is not None and mover_player_id != me.owning_player_id
                and holder.owning_player_id == me.owning_player_id and is_basic_energy_card(energy)
                and holder.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value)


card = PokemonCardDef(
    guid="cd246f41-0853-56bd-b45e-892f8bc1234c",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carbink.Name",
    display_name="Carbink",
    searchable_by=["Carbink", "Basic", "Carbink"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=703,
    abilities=[
        Ability(
            title="Energy Keeper",
            game_text="Basic Energy attached to your Basic Pok\u00e9mon can't be discarded by effects of your opponent's attacks, Abilities, or Trainer cards.",
            passive=_EnergyKeeper(),
        ),
        Attack(
            title="Stone Edge",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)