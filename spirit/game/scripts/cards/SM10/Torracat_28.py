from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="722de152-e386-5081-a193-02b64eba7246",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    display_name="Torracat",
    searchable_by=["Torracat", "Stage 1", "Torracat"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name",
    family_id=725,
    abilities=[
        Attack(
            title="Fire Fang",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)