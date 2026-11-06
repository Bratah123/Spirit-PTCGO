from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.passives_common import is_in_active_spot


class _WindCharm(Passive):
    """While this Pokemon is Active, prevent all effects of the opponent's attacks (except damage) on your Pokemon."""
    def blocks_attack_effects(self, target, carrier):
        me = carrier_pokemon(carrier)
        return me is not None and is_in_active_spot(me) and target.owning_player_id == me.owning_player_id


card = PokemonCardDef(
    guid="0962cb18-25b3-524d-b57e-2b3070b87980",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic", "Suicune"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="XY9",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=245,
    abilities=[
        Ability(
            title="Wind Charm",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, prevent all effects of your opponent's attacks, except damage, done to each of your Pok\u00e9mon. (Existing effects are not removed.)",
            passive=_WindCharm(),
        ),
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.WATER: 3},
            damage=110,
        ),
    ],
)