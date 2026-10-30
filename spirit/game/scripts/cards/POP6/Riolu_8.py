from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="fd26ddf7-5766-5b62-b86e-3698e4a2b748",
    key="POP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    display_name="Riolu",
    searchable_by=["Riolu", "Basic", "Riolu"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="POP6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=447,
    abilities=[
        Attack(
            title="Wild Kick",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)