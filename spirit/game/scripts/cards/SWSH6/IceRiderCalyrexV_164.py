from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="4aa4a917-b0d2-57bc-a397-69837cca8e5f",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IceRiderCalyrexV.Name",
    display_name="Ice Rider Calyrex V",
    searchable_by=["Ice Rider Calyrex V", "Basic", "V", "IceRiderCalyrexV"],
    subtypes=["Basic", "V"],
    collector_number=164,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=898,
    abilities=[
        Attack(
            title="Pierce",
            cost={PokemonTypes.WATER: 1},
            damage=40,
        ),
        Attack(
            title="Glacial Lance",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)