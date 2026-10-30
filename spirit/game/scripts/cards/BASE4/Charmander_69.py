from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.ecard import has_fire_energy_attached


card = PokemonCardDef(
    guid="a31d5d2f-f347-5565-90ea-25d55973a15b",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic", "Charmander"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="BASE4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Ember",
            game_text="Discard 1 Fire Energy card attached to Charmander in order to use this attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            condition=has_fire_energy_attached,
            effect=self_energy_discard_attack(
                count=1, energy_type=PokemonTypes.FIRE, before_damage=True),
        ),
    ],
)
