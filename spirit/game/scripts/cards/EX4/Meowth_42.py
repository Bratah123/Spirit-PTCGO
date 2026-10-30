from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import plunder_trainers


card = PokemonCardDef(
    guid="174a954d-b781-593a-a039-58d722864ee8",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name="Meowth",
    searchable_by=["Meowth", "Basic", "Meowth"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Attack(
            title="Plunder",
            game_text="Before doing damage, discard all Trainer cards attached to the Defending Pok\u00e9mon (before they affect the damage.).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=plunder_trainers(),
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
