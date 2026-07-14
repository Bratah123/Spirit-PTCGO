from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="ffeca5b0-67fa-5d31-9252-542983134b8b",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlazikenV.Name",
    display_name="Blaziken V",
    searchable_by=["Blaziken V", "Basic", "V", "Rapid Strike", "BlazikenV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=161,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=257,
    abilities=[
        Attack(
            title="High Jump Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=210,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)
