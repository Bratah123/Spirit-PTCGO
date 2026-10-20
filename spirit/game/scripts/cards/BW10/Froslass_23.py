from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.effects import is_special_energy


class _CursedGlarePassive(Passive):
    """As long as this Pokemon is your Active, your opponent can't attach
    Special Energy cards from their hand to their Pokemon."""

    def blocks_energy_attach(self, energy, player_id, target, carrier):
        me = carrier_pokemon(carrier)
        return (me is not None and player_id != me.owning_player_id
                and is_in_active_spot(me) and is_special_energy(energy))


card = PokemonCardDef(
    guid="cf46fabc-517c-54b7-9eb8-40fee1c867b0",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Froslass.Name",
    display_name="Froslass",
    searchable_by=["Froslass", "Stage 1", "Team Plasma", "Froslass"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=23,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Ability(
            title="Cursed Glare",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent can't attach any Special Energy cards from his or her hand to his or her Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_CursedGlarePassive(),
        ),
        Attack(
            title="Blizzard",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=spread_damage(10, also_base=True),
        ),
    ],
)