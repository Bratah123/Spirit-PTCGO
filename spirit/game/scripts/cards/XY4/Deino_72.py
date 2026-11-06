from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="a4c25feb-cdfc-538c-99ac-31680418bcb4",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name",
    display_name="Deino",
    searchable_by=["Deino", "Basic", "Deino"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="XY4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=633,
    abilities=[
        Attack(
            title="Gnaw Off",
            game_text="Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
    ],
)