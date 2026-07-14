from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive
from spirit.game.card_effects.trainers import is_basic_energy_card


class StandSentryPassive(Passive):
    def blocks_discard(self, card, carrier):
        if not is_basic_energy_card(card):
            return False
        holder = getattr(card, "parent", None)
        if holder is None or holder.owning_player_id != carrier.owning_player_id:
            return False
        area = getattr(holder, "parent", None)
        return bool(area) and area.get_attribute(AttrID.NAME) == "bench"


card = PokemonCardDef(
    guid="10c015bf-0144-5d72-b794-08a571c9cf2a",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    display_name="Hoothoot",
    searchable_by=["Hoothoot", "Basic", "Hoothoot"],
    subtypes=["Basic"],
    collector_number=120,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=163,
    abilities=[
        Ability(
            title="Stand Sentry",
            game_text="Basic Energy attached to your Benched Pok\u00e9mon can't be discarded by an effect of your opponent's Item or Supporter cards.",
            passive=StandSentryPassive(),
        ),
        Attack(
            title="Flap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)