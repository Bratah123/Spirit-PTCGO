from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import damage_per, count_in_play, self_energy_discard_attack


def _has_ability(pokemon) -> bool:
    abilities = pokemon.get_attribute(AttrID.PIE_ABILITIES) or []
    return any(isinstance(e, dict) and e.get("abilityType") in ("PokeAbility", "PokePower")
               for e in abilities)


card = PokemonCardDef(
    guid="68e23f1f-d284-5f60-88ca-fc8115f93aea",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraVMAX.Name",
    display_name="Zeraora VMAX",
    searchable_by=["Zeraora VMAX", "VMAX", "ZeraoraVMAX"],
    subtypes=["VMAX"],
    collector_number=54,
    set_code="CZ",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraV.Name",
    family_id=807,
    abilities=[
        Attack(
            title="Reactive Pulse",
            game_text="This attack does 60 damage for each of your opponent's Pok\u00e9mon in play that has an Ability.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=60,
            damage_operator="x",
            effect=damage_per(count_in_play("opponent", _has_ability), 60),
        ),
        Attack(
            title="Max Fist",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)