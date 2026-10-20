from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.session.passives import Passive, carrier_pokemon


class _MyWay(Passive):
    """If there is any Stadium card in play, this Pokemon has no Retreat Cost."""
    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        area = board.find_global_area("activeStadium")
        if carrier_pokemon(carrier) is pokemon and area and area.children:
            return 0
        return cost


card = PokemonCardDef(
    guid="12877f47-dc00-5c4c-80cf-28366611c6ce",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name",
    display_name="Cresselia",
    searchable_by=["Cresselia", "Basic", "Cresselia"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=488,
    abilities=[
        Ability(
            title="My Way",
            game_text="If there is any Stadium card in play, this Pok\u00e9mon has no Retreat Cost.",
            passive=_MyWay(),
        ),
        Attack(
            title="Moonlight Gain",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=heal_attack(20),
        ),
    ],
)