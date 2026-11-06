from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import entangle, poison_bind


card = PokemonCardDef(
    guid="abdda253-8ca1-515d-b14b-54854f12b240",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkAriados.Name",
    display_name="Dark Ariados",
    searchable_by=["Dark Ariados", "Stage 1", "DarkAriados"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=168,
    abilities=[
        Attack(
            title="Entangle",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them and switch it with the Defending Pok\u00e9mon, then flip a coin. If heads, the new Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            effect=entangle,
        ),
        Attack(
            title="Poison Bind",
            game_text="The Defending Pok\u00e9mon is now Poisoned. Flip a coin. If heads, the Defending Pok\u00e9mon can't retreat until the end of your opponent's next turn and if the effect of an attack, Pok\u00e9mon Power, or Trainer card would change that player's Active Pok\u00e9mon, that part of the effect does nothing.",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            effect=poison_bind,
        ),
    ],
)
