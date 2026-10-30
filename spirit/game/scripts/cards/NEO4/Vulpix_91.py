from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.ecard import has_fire_energy_attached


card = PokemonCardDef(
    guid="02599db7-c085-57b4-b662-49ac44603b41",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    display_name="Vulpix",
    searchable_by=["Vulpix", "Basic", "Vulpix"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=37,
    abilities=[
        Attack(
            title="Ember",
            game_text="Discard 1 Fire Energy card attached to Vulpix in order to use this attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            condition=has_fire_energy_attached,
            effect=self_energy_discard_attack(
                count=1, energy_type=PokemonTypes.FIRE, before_damage=True),
        ),
    ],
)
