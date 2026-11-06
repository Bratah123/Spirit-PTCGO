from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_per, self_energy_discard_attack, count_energy
from spirit.game.card_effects.ecard import (
    CrystalTypePassive, crystal_type_on_energy_attached,
)

card = PokemonCardDef(
    guid="d6343f67-e111-5963-9a34-a0a29bc2bc1e",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name",
    display_name="Lugia",
    searchable_by=["Lugia", "Basic", "Lugia"],
    subtypes=["Basic"],
    collector_number=149,
    set_code="ECARD2",
    rarity=Rarities.RareSecret,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=249,
    abilities=[
        Ability(
            title="Crystal Type",
            game_text="Whenever you attach a Fire, Water, or Psychic basic Energy card from your hand to Lugia, Lugia's type (color) becomes the same as that Energy card type until the end of the turn.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=CrystalTypePassive(),
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=crystal_type_on_energy_attached(
                PokemonTypes.FIRE, PokemonTypes.WATER, PokemonTypes.PSYCHIC,
            ),
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 10 damage times the number of Energy cards attached to the Defending Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(count_energy("defender", cards=True), 10),
        ),
        Attack(
            title="Steam Blast",
            game_text="Discard an Energy card attached to Lugia.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=self_energy_discard_attack(1),
        ),
    ],
)
