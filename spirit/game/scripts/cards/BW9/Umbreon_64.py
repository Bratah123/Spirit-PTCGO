from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.session.passives import Passive
from spirit.game.session.effects import is_team_plasma_pokemon


class _DarkShadePassive(Passive):
    """Each of your Team Plasma Pokemon in play gets +20 HP."""

    def max_hp_bonus(self, pokemon, carrier):
        if pokemon.owning_player_id == carrier.owning_player_id and is_team_plasma_pokemon(pokemon):
            return 20
        return 0


card = PokemonCardDef(
    guid="187da285-36e6-5ca6-a3bb-7b34e7efaad0",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon", "Stage 1", "Team Plasma", "Umbreon"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=64,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Dark Shade",
            game_text="Each of your Team Plasma Pok\u00e9mon in play gets +20 HP.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_DarkShadePassive(),
        ),
        Attack(
            title="Darkness Fang",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)