from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID
from spirit.game.session.passives import Passive


class _FightSongPassive(Passive):
    """Your Dragon Pokemon's attacks do 20 more damage to the opponent's
    Active (before Weakness and Resistance)."""

    def modify_damage_dealt(self, calc, carrier):
        attacker = calc.attacker
        if (calc.is_attack and calc.is_opposing and calc.to_active
                and attacker is not None
                and attacker.owning_player_id == carrier.owning_player_id
                and PokemonTypes.DRAGON.value in (attacker.get_attribute(AttrID.POKEMON_TYPES) or [])
                and calc.amount > 0):
            calc.amount += 20


card = PokemonCardDef(
    guid="68628e5b-da2d-518d-a85d-d792d0326160",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name",
    display_name="Altaria",
    searchable_by=["Altaria", "Stage 1", "Altaria"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Ability(
            title="Fight Song",
            game_text="Your Dragon Pok\u00e9mon's attacks do 20 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_FightSongPassive(),
        ),
        Attack(
            title="Glide",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)