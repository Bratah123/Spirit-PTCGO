from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.ecard import has_fire_energy_attached


card = PokemonCardDef(
    guid="69bcdc08-6b1d-5527-8476-69a7bd3f995e",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    display_name="Ponyta",
    searchable_by=["Ponyta", "Basic", "Ponyta"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="BASE5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=77,
    abilities=[
        Attack(
            title="Ember",
            game_text="Discard 1 Fire Energy card attached to Ponyta in order to use this attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            condition=has_fire_energy_attached,
            effect=self_energy_discard_attack(
                count=1, energy_type=PokemonTypes.FIRE, before_damage=True),
        ),
    ],
)
